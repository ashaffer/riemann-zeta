import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk4 :
    P2RoundedFactorCheckpointData.panel14Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix16_eq :
    P2RoundedFactorCheckpointData.panel14Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk4.1

theorem panel14Prefix17_eq :
    P2RoundedFactorCheckpointData.panel14Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk4.2.1

theorem panel14Prefix18_eq :
    P2RoundedFactorCheckpointData.panel14Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk4.2.2.1

theorem panel14Prefix19_eq :
    P2RoundedFactorCheckpointData.panel14Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk4.2.2.2

end RHP2Bridge
