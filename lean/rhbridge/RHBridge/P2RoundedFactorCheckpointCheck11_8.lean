import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk8 :
    P2RoundedFactorCheckpointData.panel11Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix32_eq :
    P2RoundedFactorCheckpointData.panel11Prefix32 =
      normalizedPrefixTermAtomApprox ⟨32, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk8.1

theorem panel11Prefix33_eq :
    P2RoundedFactorCheckpointData.panel11Prefix33 =
      normalizedPrefixTermAtomApprox ⟨33, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk8.2.1

theorem panel11Prefix34_eq :
    P2RoundedFactorCheckpointData.panel11Prefix34 =
      normalizedPrefixTermAtomApprox ⟨34, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk8.2.2.1

theorem panel11Prefix35_eq :
    P2RoundedFactorCheckpointData.panel11Prefix35 =
      normalizedPrefixTermAtomApprox ⟨35, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk8.2.2.2

end RHP2Bridge
