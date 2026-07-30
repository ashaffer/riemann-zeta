import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk10 :
    P2RoundedFactorCheckpointData.panel24Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix40_eq :
    P2RoundedFactorCheckpointData.panel24Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk10.1

theorem panel24Prefix41_eq :
    P2RoundedFactorCheckpointData.panel24Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk10.2.1

theorem panel24Prefix42_eq :
    P2RoundedFactorCheckpointData.panel24Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk10.2.2.1

theorem panel24Prefix43_eq :
    P2RoundedFactorCheckpointData.panel24Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk10.2.2.2

end RHP2Bridge
