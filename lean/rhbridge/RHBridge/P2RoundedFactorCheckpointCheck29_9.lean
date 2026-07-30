import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk9 :
    P2RoundedFactorCheckpointData.panel29Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix36_eq :
    P2RoundedFactorCheckpointData.panel29Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk9.1

theorem panel29Prefix37_eq :
    P2RoundedFactorCheckpointData.panel29Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk9.2.1

theorem panel29Prefix38_eq :
    P2RoundedFactorCheckpointData.panel29Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk9.2.2.1

theorem panel29Prefix39_eq :
    P2RoundedFactorCheckpointData.panel29Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk9.2.2.2

end RHP2Bridge
