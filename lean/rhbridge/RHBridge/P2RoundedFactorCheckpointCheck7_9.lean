import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk9 :
    P2RoundedFactorCheckpointData.panel7Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix36_eq :
    P2RoundedFactorCheckpointData.panel7Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk9.1

theorem panel7Prefix37_eq :
    P2RoundedFactorCheckpointData.panel7Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk9.2.1

theorem panel7Prefix38_eq :
    P2RoundedFactorCheckpointData.panel7Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk9.2.2.1

theorem panel7Prefix39_eq :
    P2RoundedFactorCheckpointData.panel7Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk9.2.2.2

end RHP2Bridge
