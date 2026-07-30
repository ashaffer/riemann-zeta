import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk2 :
    P2RoundedFactorCheckpointData.panel29Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix8_eq :
    P2RoundedFactorCheckpointData.panel29Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk2.1

theorem panel29Prefix9_eq :
    P2RoundedFactorCheckpointData.panel29Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk2.2.1

theorem panel29Prefix10_eq :
    P2RoundedFactorCheckpointData.panel29Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk2.2.2.1

theorem panel29Prefix11_eq :
    P2RoundedFactorCheckpointData.panel29Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk2.2.2.2

end RHP2Bridge
