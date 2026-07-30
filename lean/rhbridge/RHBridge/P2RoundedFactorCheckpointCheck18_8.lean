import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk8 :
    P2RoundedFactorCheckpointData.panel18Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix32_eq :
    P2RoundedFactorCheckpointData.panel18Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk8.1

theorem panel18Prefix33_eq :
    P2RoundedFactorCheckpointData.panel18Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk8.2.1

theorem panel18Prefix34_eq :
    P2RoundedFactorCheckpointData.panel18Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk8.2.2.1

theorem panel18Prefix35_eq :
    P2RoundedFactorCheckpointData.panel18Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk8.2.2.2

end RHP2Bridge
