import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk9 :
    P2RoundedFactorCheckpointData.panel6Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix36_eq :
    P2RoundedFactorCheckpointData.panel6Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk9.1

theorem panel6Prefix37_eq :
    P2RoundedFactorCheckpointData.panel6Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk9.2.1

theorem panel6Prefix38_eq :
    P2RoundedFactorCheckpointData.panel6Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk9.2.2.1

theorem panel6Prefix39_eq :
    P2RoundedFactorCheckpointData.panel6Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk9.2.2.2

end RHP2Bridge
