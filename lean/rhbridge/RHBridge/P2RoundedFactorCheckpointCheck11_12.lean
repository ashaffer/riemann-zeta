import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk12 :
    P2RoundedFactorCheckpointData.panel11Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix48_eq :
    P2RoundedFactorCheckpointData.panel11Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk12.1

theorem panel11Prefix49_eq :
    P2RoundedFactorCheckpointData.panel11Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk12.2.1

theorem panel11Prefix50_eq :
    P2RoundedFactorCheckpointData.panel11Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk12.2.2.1

theorem panel11Prefix51_eq :
    P2RoundedFactorCheckpointData.panel11Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk12.2.2.2

end RHP2Bridge
