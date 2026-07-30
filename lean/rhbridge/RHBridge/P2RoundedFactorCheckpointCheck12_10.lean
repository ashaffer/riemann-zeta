import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk10 :
    P2RoundedFactorCheckpointData.panel12Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix40_eq :
    P2RoundedFactorCheckpointData.panel12Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk10.1

theorem panel12Prefix41_eq :
    P2RoundedFactorCheckpointData.panel12Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk10.2.1

theorem panel12Prefix42_eq :
    P2RoundedFactorCheckpointData.panel12Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk10.2.2.1

theorem panel12Prefix43_eq :
    P2RoundedFactorCheckpointData.panel12Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk10.2.2.2

end RHP2Bridge
