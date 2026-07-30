import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk0 :
    P2RoundedFactorCheckpointData.panel29Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix0_eq :
    P2RoundedFactorCheckpointData.panel29Prefix0 =
      normalizedPrefixTermAtomApprox ⟨0, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk0.1

theorem panel29Prefix1_eq :
    P2RoundedFactorCheckpointData.panel29Prefix1 =
      normalizedPrefixTermAtomApprox ⟨1, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk0.2.1

theorem panel29Prefix2_eq :
    P2RoundedFactorCheckpointData.panel29Prefix2 =
      normalizedPrefixTermAtomApprox ⟨2, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk0.2.2.1

theorem panel29Prefix3_eq :
    P2RoundedFactorCheckpointData.panel29Prefix3 =
      normalizedPrefixTermAtomApprox ⟨3, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk0.2.2.2

end RHP2Bridge
