import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk9 :
    P2RoundedFactorCheckpointData.panel9Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix36_eq :
    P2RoundedFactorCheckpointData.panel9Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk9.1

theorem panel9Prefix37_eq :
    P2RoundedFactorCheckpointData.panel9Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk9.2.1

theorem panel9Prefix38_eq :
    P2RoundedFactorCheckpointData.panel9Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk9.2.2.1

theorem panel9Prefix39_eq :
    P2RoundedFactorCheckpointData.panel9Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk9.2.2.2

end RHP2Bridge
