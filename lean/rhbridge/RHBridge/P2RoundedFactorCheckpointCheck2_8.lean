import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk8 :
    P2RoundedFactorCheckpointData.panel2Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix32_eq :
    P2RoundedFactorCheckpointData.panel2Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk8.1

theorem panel2Prefix33_eq :
    P2RoundedFactorCheckpointData.panel2Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk8.2.1

theorem panel2Prefix34_eq :
    P2RoundedFactorCheckpointData.panel2Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk8.2.2.1

theorem panel2Prefix35_eq :
    P2RoundedFactorCheckpointData.panel2Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk8.2.2.2

end RHP2Bridge
