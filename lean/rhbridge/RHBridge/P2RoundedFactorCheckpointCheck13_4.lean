import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk4 :
    P2RoundedFactorCheckpointData.panel13Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix16_eq :
    P2RoundedFactorCheckpointData.panel13Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk4.1

theorem panel13Prefix17_eq :
    P2RoundedFactorCheckpointData.panel13Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk4.2.1

theorem panel13Prefix18_eq :
    P2RoundedFactorCheckpointData.panel13Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk4.2.2.1

theorem panel13Prefix19_eq :
    P2RoundedFactorCheckpointData.panel13Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk4.2.2.2

end RHP2Bridge
