import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk7 :
    P2RoundedFactorCheckpointData.panel29Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix28_eq :
    P2RoundedFactorCheckpointData.panel29Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk7.1

theorem panel29Prefix29_eq :
    P2RoundedFactorCheckpointData.panel29Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk7.2.1

theorem panel29Prefix30_eq :
    P2RoundedFactorCheckpointData.panel29Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk7.2.2.1

theorem panel29Prefix31_eq :
    P2RoundedFactorCheckpointData.panel29Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk7.2.2.2

end RHP2Bridge
