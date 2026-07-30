import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk10 :
    P2RoundedFactorCheckpointData.panel10Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix40_eq :
    P2RoundedFactorCheckpointData.panel10Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk10.1

theorem panel10Prefix41_eq :
    P2RoundedFactorCheckpointData.panel10Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk10.2.1

theorem panel10Prefix42_eq :
    P2RoundedFactorCheckpointData.panel10Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk10.2.2.1

theorem panel10Prefix43_eq :
    P2RoundedFactorCheckpointData.panel10Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk10.2.2.2

end RHP2Bridge
