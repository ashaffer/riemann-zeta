import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk2 :
    P2RoundedFactorCheckpointData.panel31Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix8_eq :
    P2RoundedFactorCheckpointData.panel31Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk2.1

theorem panel31Prefix9_eq :
    P2RoundedFactorCheckpointData.panel31Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk2.2.1

theorem panel31Prefix10_eq :
    P2RoundedFactorCheckpointData.panel31Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk2.2.2.1

theorem panel31Prefix11_eq :
    P2RoundedFactorCheckpointData.panel31Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk2.2.2.2

end RHP2Bridge
