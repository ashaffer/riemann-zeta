import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk8 :
    P2RoundedFactorCheckpointData.panel1Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix32_eq :
    P2RoundedFactorCheckpointData.panel1Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk8.1

theorem panel1Prefix33_eq :
    P2RoundedFactorCheckpointData.panel1Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk8.2.1

theorem panel1Prefix34_eq :
    P2RoundedFactorCheckpointData.panel1Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk8.2.2.1

theorem panel1Prefix35_eq :
    P2RoundedFactorCheckpointData.panel1Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk8.2.2.2

end RHP2Bridge
