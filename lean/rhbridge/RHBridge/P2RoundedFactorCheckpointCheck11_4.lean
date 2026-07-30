import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk4 :
    P2RoundedFactorCheckpointData.panel11Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix16_eq :
    P2RoundedFactorCheckpointData.panel11Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk4.1

theorem panel11Prefix17_eq :
    P2RoundedFactorCheckpointData.panel11Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk4.2.1

theorem panel11Prefix18_eq :
    P2RoundedFactorCheckpointData.panel11Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk4.2.2.1

theorem panel11Prefix19_eq :
    P2RoundedFactorCheckpointData.panel11Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk4.2.2.2

end RHP2Bridge
