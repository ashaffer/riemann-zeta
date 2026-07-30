import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk10 :
    P2RoundedFactorCheckpointData.panel7Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix40_eq :
    P2RoundedFactorCheckpointData.panel7Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk10.1

theorem panel7Prefix41_eq :
    P2RoundedFactorCheckpointData.panel7Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk10.2.1

theorem panel7Prefix42_eq :
    P2RoundedFactorCheckpointData.panel7Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk10.2.2.1

theorem panel7Prefix43_eq :
    P2RoundedFactorCheckpointData.panel7Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk10.2.2.2

end RHP2Bridge
