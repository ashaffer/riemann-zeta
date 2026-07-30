import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk4 :
    P2RoundedFactorCheckpointData.panel29Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix16_eq :
    P2RoundedFactorCheckpointData.panel29Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk4.1

theorem panel29Prefix17_eq :
    P2RoundedFactorCheckpointData.panel29Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk4.2.1

theorem panel29Prefix18_eq :
    P2RoundedFactorCheckpointData.panel29Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk4.2.2.1

theorem panel29Prefix19_eq :
    P2RoundedFactorCheckpointData.panel29Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk4.2.2.2

end RHP2Bridge
