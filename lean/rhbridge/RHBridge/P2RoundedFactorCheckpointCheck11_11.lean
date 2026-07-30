import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk11 :
    P2RoundedFactorCheckpointData.panel11Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix44_eq :
    P2RoundedFactorCheckpointData.panel11Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk11.1

theorem panel11Prefix45_eq :
    P2RoundedFactorCheckpointData.panel11Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk11.2.1

theorem panel11Prefix46_eq :
    P2RoundedFactorCheckpointData.panel11Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk11.2.2.1

theorem panel11Prefix47_eq :
    P2RoundedFactorCheckpointData.panel11Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk11.2.2.2

end RHP2Bridge
