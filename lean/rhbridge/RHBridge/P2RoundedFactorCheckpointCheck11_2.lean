import RHBridge.P2RoundedFactorCheckpointData11

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FactorChunk2 :
    P2RoundedFactorCheckpointData.panel11Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨11, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel11Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨11, by decide⟩ := by
  decide +kernel

theorem panel11Prefix8_eq :
    P2RoundedFactorCheckpointData.panel11Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk2.1

theorem panel11Prefix9_eq :
    P2RoundedFactorCheckpointData.panel11Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk2.2.1

theorem panel11Prefix10_eq :
    P2RoundedFactorCheckpointData.panel11Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk2.2.2.1

theorem panel11Prefix11_eq :
    P2RoundedFactorCheckpointData.panel11Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨11, by decide⟩ := by
  exact panel11FactorChunk2.2.2.2

end RHP2Bridge
