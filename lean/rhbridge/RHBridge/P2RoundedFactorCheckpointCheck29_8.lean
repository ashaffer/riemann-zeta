import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk8 :
    P2RoundedFactorCheckpointData.panel29Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix32_eq :
    P2RoundedFactorCheckpointData.panel29Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk8.1

theorem panel29Prefix33_eq :
    P2RoundedFactorCheckpointData.panel29Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk8.2.1

theorem panel29Prefix34_eq :
    P2RoundedFactorCheckpointData.panel29Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk8.2.2.1

theorem panel29Prefix35_eq :
    P2RoundedFactorCheckpointData.panel29Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk8.2.2.2

end RHP2Bridge
